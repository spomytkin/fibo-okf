---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sovereign debt instrument
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt security issued by the government of a country
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: Nf0cdedde869546f0b49328649bb2b623
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignDebtInstrument
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: sovereign debt instrument
type: Ontology Class
---

# sovereign debt instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignDebtInstrument>

## Definition

debt security issued by the government of a country

## Relationships

- **Subclass of**: [GovernmentIssuedDebtSecurity](/concepts/fibo/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from value `Nf0cdedde869546f0b49328649bb2b623`

## Annotations

- **label**: sovereign debt instrument
- **definition**: debt security issued by the government of a country

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
