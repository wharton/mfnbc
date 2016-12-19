import nltk
import csv
import os


class MFNBC:
    """A Multi-Function Naive Bayes Classifier"""

    def __init__(self, likelihoods_input_file, unlabeled_data_file, verbose):
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
        self.verbose = verbose
        self.probs = {}
        self.posteriors = {}
        self.features = []
        self.outfile = 'out_{}'.format(self.unlabeled_data_file)

    def write_csv(self):
        self._read_likelihoods()
        self._process_unlabeled()
        print("wrote {}".format(self.outfile))

    def print_probs(self):
        if len(self.probs.items()) == 0:
            self._read_likelihoods()
        print(self.probs)
        for k, v in self.probs.items():
            print("Word: {} | Likelihoods: {}".format(k, v))

    def _read_likelihoods(self):
        with open(self.likelihoods_input_file,
                  'r', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.probs[row['Word']] = row
            self.features = reader.fieldnames
            self.features.remove('Word')
            for f in self.features:
                    self.posteriors[f] = 1 / len(self.features)
            self.print_probs() if self.verbose else None

    def _calc_denuminator(self, posteriors, prob_row, features):
        den = 0
        for f in self.features:
            den += (posteriors[f] * float(prob_row[f]))
        return den

    def fooz(self):
        1 + 1

    def _process_unlabeled(self):
        with open(self.unlabeled_data_file,
                  'r', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                if i % 10 == 0:
                    print(i) if self.verbose else None
                sen = row['Text']
                tokens = nltk.word_tokenize(sen)
                for tok in tokens:
                    lowered_tok = tok.lower()
                    if lowered_tok in self.probs:
                        prob_row = self.probs[lowered_tok]
                        den = self._calc_denuminator(
                            self.posteriors, prob_row, self.features)
                        for f in self.features:
                            num = (self.posteriors[f] * float(prob_row[f]))
                            res = num / den
                            self.posteriors[f] = res
                for key, pos in self.posteriors.items():
                    print("Current Posteriors {} - {}".format(key, pos)
                          ) if self.verbose else None
                    row[key] = pos
                fieldnames = reader.fieldnames + self.features
                file_exists = os.path.isfile(self.outfile)
                with open(self.outfile, 'a', encoding='ISO-8859-1') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(row)


# m = MFNBC('likeli_sample.csv', 'input_sample.csv', False)
# m._read_likelihoods()
# m._process_unlabeled()
