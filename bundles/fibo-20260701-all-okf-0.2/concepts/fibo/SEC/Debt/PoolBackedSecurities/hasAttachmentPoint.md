---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has attachment point
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the minimum (lower boundary) of the total value of the underlying collateral, either at issuance or as
      of some point in time, at which point a given tranche becomes liable for losses
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: When it is said that a tranche becomes 'liable for losses,' it means that the tranche starts to absorb or incur
      financial losses due to defaults or impairments in the underlying assets. This is based on the contractual agreements
      and the structuring of the CDO, which dictate the order in which losses are allocated to different tranches. Note that
      the notion of 'liability for loss' is in a financial or econonmic sense rather than a legal sense.
  range:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/AttachmentPoint.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AttachmentPoint
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/hasAttachmentPoint
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: has attachment point
type: Ontology Property
---

# has attachment point

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/hasAttachmentPoint>

## Definition

indicates the minimum (lower boundary) of the total value of the underlying collateral, either at issuance or as of some point in time, at which point a given tranche becomes liable for losses

## Relationships

- **Range**: [AttachmentPoint](/concepts/fibo/SEC/Debt/PoolBackedSecurities/AttachmentPoint.md)
- **Subproperty of**: [hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)

## Annotations

- **label**: has attachment point
- **definition**: indicates the minimum (lower boundary) of the total value of the underlying collateral, either at issuance or as of some point in time, at which point a given tranche becomes liable for losses
- **explanatoryNote** (en): When it is said that a tranche becomes 'liable for losses,' it means that the tranche starts to absorb or incur financial losses due to defaults or impairments in the underlying assets. This is based on the contractual agreements and the structuring of the CDO, which dictate the order in which losses are allocated to different tranches. Note that the notion of 'liability for loss' is in a financial or econonmic sense rather than a legal sense.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
