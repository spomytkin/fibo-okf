---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: inflation-linked bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond indexed to inflation so that the principal or interest payments rise and fall with the rate of inflation
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ILB
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Inflation-linked bonds are primarily issued by sovereign governments, such as the U.S. and the UK.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: inflation-indexed bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InflationRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/IndexLinkedBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/IndexLinkedBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/InflationLinkedBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: inflation-linked bond
type: Ontology Class
---

# inflation-linked bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/InflationLinkedBond>

## Definition

bond indexed to inflation so that the principal or interest payments rise and fall with the rate of inflation

## Relationships

- **Subclass of**: [IndexLinkedBond](/concepts/fibo/SEC/Debt/Bonds/IndexLinkedBond.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [InflationRate](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InflationRate.md)

## Annotations

- **label**: inflation-linked bond
- **definition**: bond indexed to inflation so that the principal or interest payments rise and fall with the rate of inflation
- **abbreviation**: ILB
- **explanatoryNote**: Inflation-linked bonds are primarily issued by sovereign governments, such as the U.S. and the UK.
- **synonym**: inflation-indexed bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
