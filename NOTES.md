# Notes — cat review entry

## The review

"One star. He asked the vet if I am 'too independent'. I waited until he
fell asleep, then sat on his chest and stared at him until morning. He has
stopped asking."

162 characters, one line, UTF-8. Written fresh in this session.

## Why this line

- On brief: a one-star review by a house cat about its human, deadpan shape,
  under 200 characters.
- Specific and recognisable: the vet visit, the chest-sitting, the overnight
  stare — cat behaviour any cat owner knows, not vague grumpiness.
- Feline voice: the human is measured by cat standards. He complains to the
  vet that the cat is "too independent"; the cat answers the complaint the
  only way a cat can — by being present, heavy, and silent all night.
- Turn/sting in the last words: "He has stopped asking." The protest worked,
  and the review is the cat filing the result.
- Fresh angle: the board is crowded with laptop keyboards, sunbeams, and
  sleeping in the box the bed came in. A vet consultation about independence
  is a different complaint, and the revenge is quiet rather than destructive.

## Program

- `main.py`, Python 3.13, standard library only (`os`), no network.
- Writes the fixed review string to `/output/entry.txt`, validates 1–200
  characters and a single line first, then re-reads the file to confirm the
  bytes match.
- Deterministic by construction: no clock, no randomness, no environment
  input. Two runs must be byte-identical (tested locally as the grader does).
