# req-audit — reviewer personas for a requirements document

PYTHON ?= python3
TEMPLATE ?=

.PHONY: all sync check check-template clean help

all: sync

## sync: materialise shared/ into every skill's references/
sync:
	$(PYTHON) scripts/sync.py

## check: validate the catalogue (frontmatter, coverage, freshness, portability)
check:
	$(PYTHON) scripts/validate.py $(if $(TEMPLATE),--template $(TEMPLATE),)

## check-template: also cross-check the section inventory against the upstream template
check-template:
	@test -n "$(TEMPLATE)" || { echo "usage: make check-template TEMPLATE=../cas-handbook-req-template"; exit 2; }
	$(PYTHON) scripts/validate.py --template $(TEMPLATE)

## clean: remove the generated copies under skills/*/references/
clean:
	@find skills -maxdepth 3 -name '*.md' -exec grep -l '^<!-- GENERATED from shared/' {} + | xargs -r rm -v

## help: list targets
help:
	@grep -E '^## ' Makefile | sed 's/^## /  /'
