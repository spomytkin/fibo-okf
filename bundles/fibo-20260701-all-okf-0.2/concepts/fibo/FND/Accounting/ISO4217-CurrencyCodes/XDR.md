---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: XDR
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the IMF's identifier for SDR (Special Drawing Right)
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: XDR
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/UnitOfAccountIdentifier
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/ISO4217-CodeSet.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/ISO4217-CodeSet
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/SDR_SpecialDrawingRight.md
    predicate: https://www.omg.org/spec/Commons/Designators/denotes
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/SDR_SpecialDrawingRight
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/SDR_SpecialDrawingRight.md
    predicate: https://www.omg.org/spec/Commons/Identifiers/identifies
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/SDR_SpecialDrawingRight
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/XDR
sources:
- id: fibo-source-4a323fa733
  resource: references/fibo/FND/Accounting/ISO4217-CurrencyCodes.rdf
  sha256: 4a323fa7336e398c312a7f8afc057b57c4a92078063cdd27a8ff11fc1fe0d60c
  title: FIBO source FND/Accounting/ISO4217-CurrencyCodes.rdf
title: XDR
type: Ontology Individual
---

# XDR

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/XDR>

## Definition

the IMF's identifier for SDR (Special Drawing Right)

## Relationships

- **Related to**: [ISO4217-CodeSet](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/ISO4217-CodeSet.md)
- **Related to**: [SDR_SpecialDrawingRight](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/SDR_SpecialDrawingRight.md)
- **Related to**: [SDR_SpecialDrawingRight](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/SDR_SpecialDrawingRight.md)

## Annotations

- **label**: XDR
- **definition** (en): the IMF's identifier for SDR (Special Drawing Right)
- **hasTag**: XDR

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
