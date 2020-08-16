from difflib import get_close_matches, SequenceMatcher
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--title', default='machine learning', help="Job title.")
parser.add_argument('--threshold', default=0.5, type=float, help="Minimum threshold for the similarity.")
parser.add_argument('--top', default=5, type=int, help="Number of top results.")
args = parser.parse_args()

def ratio_filter(e):
    return e[0]

def main(title, df, top):
    total = len(df)
    tmp = set(df.title[df.title.str.contains(title)].to_list() +\
          get_close_matches(title, df['title']))

    ratio = [(SequenceMatcher(None, title, x).ratio(), x) for x in tmp]
    ratio = sorted(ratio, key=ratio_filter, reverse=True)
    print('\nTotal Jobs in dataset:', total, '\n')
    c = 0
    flag = True
    for x in ratio:
        if x[0] > args.threshold:
            flag = False
            tmp_tot = len(df[df.title == x[1]])
            print(x[1])
            print('Probability: {:.5f}'.format(tmp_tot/total), ' |  Count:', tmp_tot,\
                  ' |  Similarity: {:.5f}'.format(x[0]), '\n')
            c += 1
        if c == args.top:
            break

    if len(ratio) == 0 or flag:
        print('No jobs title similar to "%s".' % title)


if __name__ == "__main__":
    print('\nArguments:')
    for arg in vars(args):
        print(arg, '-', getattr(args, arg))
    df = pd.read_csv('data/indeed.csv')
    main(args.title.lower(), df, args.top)
