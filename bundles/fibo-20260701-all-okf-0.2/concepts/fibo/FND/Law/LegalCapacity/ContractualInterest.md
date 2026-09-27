---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual interest
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legally enforceable benefit or entitlement arising from a contract, agreement, or instrument, in which an entity
      holds specified rights or obligations related to the performance, use, or benefit of something, without necessarily
      holding ownership
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Contractual interest may include rights to income, access, use, or participation, and is governed by the terms
      and conditions of the underlying contract. It may be transferable or limited, and can coexist with or be independent
      of ownership rights.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Contractual interests differ from ownership interests in terms of (1) the source of rights, which are specified
      in an agreement or contract in the case of contractual interests, and in terms of title or equity with respect to ownership,
      (2) control, which is typically limited at best in the case of contractual interest, and (3) transferability, which
      depends on the terms of the contract. Examples of contractual interest include fund units, leaseholds, annuities, and
      rights to certain services, whereas shares, real estate, and assets of a trust reflect ownership interest.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/hasFractionalInterest
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/ContractualRight.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualRight
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualInterest
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: contractual interest
type: Ontology Class
---

# contractual interest

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualInterest>

## Definition

legally enforceable benefit or entitlement arising from a contract, agreement, or instrument, in which an entity holds specified rights or obligations related to the performance, use, or benefit of something, without necessarily holding ownership

## Relationships

- **Subclass of**: [ContractualRight](/concepts/fibo/FND/Law/LegalCapacity/ContractualRight.md)

## Constraints

- **[hasFractionalInterest](/concepts/fibo/FND/Law/LegalCapacity/hasFractionalInterest.md)**: min qualified cardinality 0 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: contractual interest
- **definition**: legally enforceable benefit or entitlement arising from a contract, agreement, or instrument, in which an entity holds specified rights or obligations related to the performance, use, or benefit of something, without necessarily holding ownership
- **explanatoryNote**: Contractual interest may include rights to income, access, use, or participation, and is governed by the terms and conditions of the underlying contract. It may be transferable or limited, and can coexist with or be independent of ownership rights.
- **explanatoryNote**: Contractual interests differ from ownership interests in terms of (1) the source of rights, which are specified in an agreement or contract in the case of contractual interests, and in terms of title or equity with respect to ownership, (2) control, which is typically limited at best in the case of contractual interest, and (3) transferability, which depends on the terms of the contract. Examples of contractual interest include fund units, leaseholds, annuities, and rights to certain services, whereas shares, real estate, and assets of a trust reflect ownership interest.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
