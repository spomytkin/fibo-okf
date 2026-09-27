---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: product disclosure requirement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A requirement governing what representations can be made about a product, as it affects the consumer.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There are also rules which encompass limitations on how you might attach loans and liens to principle dwellings,
      e.g. when or whether you can foreclose on someone's principal dwelling with impunity; what rights the consumer has -
      this last will be a separate kind of regulation.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/GoodFaithEstimate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/LoanProductRepresentations
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRequirement
sources:
- id: fibo-source-9d1d4cf0d4
  resource: references/fibo/LOAN/LoansGeneral/LoansRegulatory.rdf
  sha256: 9d1d4cf0d45e2966f6fbe27dd62486cdd11c427c2d40f7701ea8f1775769245b
  title: FIBO source LOAN/LoansGeneral/LoansRegulatory.rdf
title: product disclosure requirement
type: Ontology Class
---

# product disclosure requirement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRequirement>

## Definition

A requirement governing what representations can be made about a product, as it affects the consumer.

## Relationships

- **Subclass of**: [DisclosureRequirement](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement.md)

## Constraints

- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [GoodFaithEstimate](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/GoodFaithEstimate.md)
- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [LoanProductRepresentations](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/LoanProductRepresentations.md)

## Annotations

- **label** (en): product disclosure requirement
- **definition** (en): A requirement governing what representations can be made about a product, as it affects the consumer.
- **explanatoryNote** (en): There are also rules which encompass limitations on how you might attach loans and liens to principle dwellings, e.g. when or whether you can foreclose on someone's principal dwelling with impunity; what rights the consumer has - this last will be a separate kind of regulation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
