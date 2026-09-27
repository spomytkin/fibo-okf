---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is compounded
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Definition needed Moved from Yield - assume this can only be about debt instrument or loan / debt yields i..e where
      the income relates to interest payments. .
  domain:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/isCompounded
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: is compounded
type: Ontology Property
---

# is compounded

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/isCompounded>

## Definition

Definition needed Moved from Yield - assume this can only be about debt instrument or loan / debt yields i..e where the income relates to interest payments. .

## Relationships

- **Domain**: [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is compounded
- **definition** (en): Definition needed Moved from Yield - assume this can only be about debt instrument or loan / debt yields i..e where the income relates to interest payments. .

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
