.PHONY: fetch

fetch:
	./ops/data.sh
	./ops/normalise.py cmudict-0.7b

