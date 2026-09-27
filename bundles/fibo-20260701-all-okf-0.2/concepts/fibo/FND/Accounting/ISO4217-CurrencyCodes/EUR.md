---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: EUR
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the currency identifier for Euro
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: EUR
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CurrencyIdentifier
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/Euro.md
    predicate: https://www.omg.org/spec/Commons/Designators/denotes
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/Euro
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/Euro.md
    predicate: https://www.omg.org/spec/Commons/Identifiers/identifies
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/Euro
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/ISO4217-CodeSet.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/ISO4217-CodeSet
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/EUR
sources:
- id: fibo-source-4a323fa733
  resource: references/fibo/FND/Accounting/ISO4217-CurrencyCodes.rdf
  sha256: 4a323fa7336e398c312a7f8afc057b57c4a92078063cdd27a8ff11fc1fe0d60c
  title: FIBO source FND/Accounting/ISO4217-CurrencyCodes.rdf
title: EUR
type: Ontology Individual
---

# EUR

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/EUR>

## Definition

the currency identifier for Euro

## Relationships

- **Related to**: [ISO4217-CodeSet](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/ISO4217-CodeSet.md)
- **Related to**: [Euro](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/Euro.md)
- **Related to**: [Euro](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/Euro.md)

## Annotations

- **label**: EUR
- **definition** (en): the currency identifier for Euro
- **hasTag**: EUR

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
