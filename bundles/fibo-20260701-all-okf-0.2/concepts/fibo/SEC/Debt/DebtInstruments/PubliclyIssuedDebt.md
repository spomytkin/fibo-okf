---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: publicly issued debt
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an issued debt in the form of a tradable debt instrument (security)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/IssuedDebt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/IssuedDebt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PubliclyIssuedDebt
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: publicly issued debt
type: Ontology Class
---

# publicly issued debt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PubliclyIssuedDebt>

## Definition

an issued debt in the form of a tradable debt instrument (security)

## Relationships

- **Subclass of**: [IssuedDebt](/concepts/fibo/SEC/Debt/DebtInstruments/IssuedDebt.md)

## Constraints

- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: all values from of type [TradableDebtInstrument](/concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)

## Annotations

- **label**: publicly issued debt
- **definition**: an issued debt in the form of a tradable debt instrument (security)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
