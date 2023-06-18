import argparse
from nltk.corpus import stopwords
import numpy as np
import statistics


# Compute Non-Monotonicty as Alignment Deviation from the Diagonal
def non_monotonicity_score(positions):
    scores = []
    for p in positions:
        if len(p) == 0:
            continue
        n_pos = len(p)
        abs_diff = sum([abs(num[0] - num[1]) for num in p])
        scores.append((abs_diff / n_pos) * 100)

    return statistics.mean(scores)


# Read the Alignments and Collect Scoring Information
def read_alignments(source_words, target_words, align_file):
    f = open(align_file, "r")
    i, aligned_positions, unaligned_source_words = 0, [], []

    for line in f:
        temp_aligned_positions, unaligned_source_positions = [], []
        aligned_source_positions = [int(y.split("-")[0]) for y in line.strip().split()]
        source_length = len(source_words[i])

        # Save the position of Word Alignments
        target_length = len(target_words[i])
        if source_length == 0 or target_length == 0:
            pass
        else:
            temp_aligned_positions = [
                (
                    (int(y.split("-")[0]) + 1) / source_length,
                    (int(y.split("-")[1]) + 1) / target_length,
                )
                for y in line.strip().split()
            ]
        aligned_positions.append(temp_aligned_positions)

        # Check if all source word positions are aligned
        for x in range(source_length):
            if x not in aligned_source_positions:
                unaligned_source_positions.append(x)

        unaligned_source_words.append(unaligned_source_positions)
        i = i + 1

    f.close()

    return aligned_positions, unaligned_source_words


def process_files(source_file, align_file, target_file):
    # Read the Source File
    with open(source_file, "r") as f:
        source_words = list(map(lambda line: line.strip().split(), f.readlines()))

    # Read the Target File
    with open(target_file, "r") as f:
        target_words = list(map(lambda line: line.strip().split(), f.readlines()))

    # Read the Alignments
    aligned_positions, unaligned_source_words = read_alignments(
        source_words, target_words, align_file
    )

    usw_scores_micro = [
        len(x) / len(y) for x, y in zip(unaligned_source_words, source_words)
    ]
    total_words_macro = sum([len(x) for x in source_words])
    unaligned_source_words_macro = sum([len(x) for x in unaligned_source_words])

    print(
        "Macro Unaligned-Source-Words (USW) Score = ",
        (unaligned_source_words_macro / total_words_macro) * 100,
    )
    print("Non-Monotonicty (NM) Score = ", non_monotonicity_score(aligned_positions))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get USW and NM Scores.")
    parser.add_argument("source_file", type=str, help="Source file")
    parser.add_argument("align_file", type=str, help="Alignment file")
    parser.add_argument("target_file", type=str, help="Target file")

    args = parser.parse_args()

    process_files(args.source_file, args.align_file, args.target_file)
