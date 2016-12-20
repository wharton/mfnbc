import nltk
import csv
import os


class MFNBC:
    """A Multi-Function Naive Bayes Classifier"""

    def __init__(self, likelihoods_input_file, unlabeled_data_file,
                 verbose, output_filename='out.csv'):
        """
            Args:
                likelihoods_input_file - location of Likelyhood table (str)
                unlabeled_data_file - Location of unlabeled data file (str)
                verbose - Turn on of off verbolse output,
                    Default is false (boolean)
            Returns:
                None
        """
        self.likelihoods_input_file = likelihoods_input_file
        self.unlabeled_data_file = unlabeled_data_file
        self.outfile = output_filename
        self.verbose = verbose
        self.probs = {}
        self.posteriors = {}
        self.results = []
        self.features = []
        self.fieldnames = None
        print("Checking if you have NLTK libs...")
        nltk.download('punkt')


    def calc_posteriors(self):
        """
        A Public function calculate the postiros for a list of texts
        """
        if len(self.probs.items()) == 0:
            self.read_likelihoods()
        return self._process_unlabeled()


    def write_csv(self):
        print("Writing CSV file: {}".format(self.outfile))
        """
        A Public function to write the CSV
                Args: self
        Returns:
            None
        # """
        if len(self.probs.items()) == 0:
            self.read_likelihoods()
            self.calc_posteriors()
        for row in self.results:
            file_exists = os.path.isfile(self.outfile)
            with open(self.outfile, 'a', encoding='ISO-8859-1') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(row)
        print("Finished writing: {}".format(self.outfile))

    def print_likelyhoods(self):
        if len(self.probs.items()) == 0:
            self.read_likelihoods()
        for k, v in self.probs.items():
            print("Word: {} | Likelihoods: {}".format(k, v))

    def read_likelihoods(self):
        print("Reading Likelihoods")
        with open(self.likelihoods_input_file,
                  'r', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.probs[row['Word']] = row
            self.features = reader.fieldnames
            self.features.remove('Word')
            for f in self.features:
                self.posteriors[f] = 1 / len(self.features)
            self.print_likelyhoods() if self.verbose else None
        return self.probs

    def _calc_denominator(self, prob_row):
        den = 0
        for f in self.features:
            den += (self.posteriors[f] * float(prob_row[f]))
        return den

    def _process_unlabeled(self):
        print("Processing Unlabeled Texts...")
        with open(self.unlabeled_data_file,
                  'r', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            if not self.fieldnames:
                self.fieldnames = reader.fieldnames + self.features
            for index, row in enumerate(reader):
                for f in self.features:
                    self.posteriors[f] = 1 / len(self.features)
                if index % 10 == 0 and index > 1:
                    print("Completed {} texts".format(index))
                text = row['Text']
                tokens = nltk.word_tokenize(text)
                for tok in tokens:
                    lowered_tok = tok.lower()
                    if lowered_tok in self.probs:
                        prob_row = self.probs[lowered_tok]
                        denominator = self._calc_denominator(prob_row)
                        for f in self.features:
                            num = (self.posteriors[f] * float(prob_row[f]))
                            res = num / denominator
                            self.posteriors[f] = res
                for key, pos in self.posteriors.items():
                    print("Current Posteriors {} - {}".format(key, pos)
                          ) if self.verbose else None
                    row[key] = pos
                self.results.append(row)
        return self.results


# m = MFNBC('sample_files/likeli_sample.csv',
          # 'sample_files/input_sample.csv', False).write_csv()
# m.read_likelihoods()
# x = m.calc_posteriors()
# # print(x)
# m.write_csv()
