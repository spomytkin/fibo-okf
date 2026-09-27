---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: segment of a pool of securities, typically debt instruments
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A tranche is one of a number of related securities in the same offering that represents a partition of a debt pool
      whose cash flow is derived from the combined cash flows of the instruments in that partition.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AttachmentPoint
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/hasAttachmentPoint
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DetachmentPoint
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/hasDetachmentPoint
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/hasEstimatedTotalCollateralValueAtIssuance
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
    value: N736f8e0df4384b209f63bd5167ced0f4
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/Tranche
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: tranche
type: Ontology Class
---

# tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/Tranche>

## Definition

segment of a pool of securities, typically debt instruments

## Relationships

- **Subclass of**: [StructuredFinanceInstrument](/concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md)

## Constraints

- **[hasAttachmentPoint](/concepts/fibo/SEC/Debt/PoolBackedSecurities/hasAttachmentPoint.md)**: min qualified cardinality 0 of type [AttachmentPoint](/concepts/fibo/SEC/Debt/PoolBackedSecurities/AttachmentPoint.md)
- **[hasDetachmentPoint](/concepts/fibo/SEC/Debt/PoolBackedSecurities/hasDetachmentPoint.md)**: min qualified cardinality 0 of type [DetachmentPoint](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DetachmentPoint.md)
- **[hasEstimatedTotalCollateralValueAtIssuance](/concepts/fibo/SEC/Debt/PoolBackedSecurities/hasEstimatedTotalCollateralValueAtIssuance.md)**: min qualified cardinality 0 of type [CollateralValueAsOfDate](/concepts/fibo/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from value `N736f8e0df4384b209f63bd5167ced0f4`

## Annotations

- **label** (en): tranche
- **definition** (en): segment of a pool of securities, typically debt instruments
- **explanatoryNote** (en): A tranche is one of a number of related securities in the same offering that represents a partition of a debt pool whose cash flow is derived from the combined cash flows of the instruments in that partition.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
