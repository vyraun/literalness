Code for the metrics used in "**[Do GPTs Produce Less Literal Translations?](https://arxiv.org/abs/2305.16806)**" (ACL 2023).

Get alignments from [vyraun/awesome-align](https://github.com/vyraun/awesome-align), which is a fork of [neulab/awesome-align](https://github.com/neulab/awesome-align).

```bash
bash extractv3.sh source_file target_file
```

This will produce a `.aligned` file with alignments in the Pharaoh (i-j) format.

Then, use `compute_scores.py` to get the USW and NM scores.

```bash
python compute_scores.py source_file alignment_file target_file
```

If you find our code or paper useful, please cite the paper:
```
@inproceedings{raunak-etal-gpt-literalness,
    title = "Do GPTs Produce Less Literal Translations?",
    author = "Raunak, Vikas and Arul, Menezes and Post, Matt and Awadalla, Hany Hassan",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics",
    publisher = "Association for Computational Linguistics",
    year = "2023"
}
```
