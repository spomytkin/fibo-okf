---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: treasury bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: long term term coupon bearing treasury obligation issued in terms of 20 years or 30 years that pays interest every
      six months until they mature
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.treasurydirect.gov/indiv/research/indepth/tbonds/res_tbond.htm
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/SovereignBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/USTreasurySecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/USTreasurySecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: treasury bond
type: Ontology Class
---

# treasury bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryBond>

## Definition

long term term coupon bearing treasury obligation issued in terms of 20 years or 30 years that pays interest every six months until they mature

## Relationships

- **See also**: [res_tbond.htm](<https://www.treasurydirect.gov/indiv/research/indepth/tbonds/res_tbond.htm>)
- **Subclass of**: [SovereignBond](/concepts/fibo/SEC/Debt/Bonds/SovereignBond.md)
- **Subclass of**: [USTreasurySecurity](/concepts/fibo/SEC/Debt/Bonds/USTreasurySecurity.md)

## Annotations

- **label**: treasury bond
- **definition**: long term term coupon bearing treasury obligation issued in terms of 20 years or 30 years that pays interest every six months until they mature

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
