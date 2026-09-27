---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SLE
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the currency identifier for Leone
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: The Sierra Leonean LEONE (SLL) is redenominated by removing three (3) zeros from the denominations. A new currency
      code SLE/925 representing the new valuation (1,000 times old SLL/694) is introduced on 1st April 2022 for any internal
      needs during the redenomination process, and is replacing SLL as the official currency code, after the transition period
      to be determined. During this transition period, both the old Leone and new Leone will be in physical circulation for
      at least 90 days. The Bank of Sierra Leone will adopt the new code in the local system but SLL/694 shall remain in use
      until further notice. The Sierra Leonean currency shall continue to be the LEONE and this will not change after redenomination.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: SLE
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CurrencyIdentifier
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/ISO4217-CodeSet.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/ISO4217-CodeSet
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/Leone.md
    predicate: https://www.omg.org/spec/Commons/Designators/denotes
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/Leone
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/Leone.md
    predicate: https://www.omg.org/spec/Commons/Identifiers/identifies
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/Leone
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/SLE
sources:
- id: fibo-source-4a323fa733
  resource: references/fibo/FND/Accounting/ISO4217-CurrencyCodes.rdf
  sha256: 4a323fa7336e398c312a7f8afc057b57c4a92078063cdd27a8ff11fc1fe0d60c
  title: FIBO source FND/Accounting/ISO4217-CurrencyCodes.rdf
title: SLE
type: Ontology Individual
---

# SLE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/SLE>

## Definition

the currency identifier for Leone

## Relationships

- **Related to**: [ISO4217-CodeSet](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/ISO4217-CodeSet.md)
- **Related to**: [Leone](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/Leone.md)
- **Related to**: [Leone](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/Leone.md)

## Annotations

- **label**: SLE
- **definition** (en): the currency identifier for Leone
- **note** (en): The Sierra Leonean LEONE (SLL) is redenominated by removing three (3) zeros from the denominations. A new currency code SLE/925 representing the new valuation (1,000 times old SLL/694) is introduced on 1st April 2022 for any internal needs during the redenomination process, and is replacing SLL as the official currency code, after the transition period to be determined. During this transition period, both the old Leone and new Leone will be in physical circulation for at least 90 days. The Bank of Sierra Leone will adopt the new code in the local system but SLL/694 shall remain in use until further notice. The Sierra Leonean currency shall continue to be the LEONE and this will not change after redenomination.
- **hasTag**: SLE

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
