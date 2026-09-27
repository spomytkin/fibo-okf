---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund legal form documentation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: For a fund which is constituted under the law of contract, the constitution or articles that define the fund. These
      are embodied in a Contract.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'From ISO FIBIM "Umbrella Fund" narrative: In securities, a collective investment scheme that has a contractual
      or a corporate form. When it has a contractual form, a fund is constituted under either the law of contract or under
      the trust law and thus it is not a legal entity. In its corporate form, a fund is a legal entity and is structured as
      a company.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCore/Constitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/Constitution
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundLegalFormDocumentation
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund legal form documentation
type: Ontology Class
---

# fund legal form documentation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundLegalFormDocumentation>

## Definition

For a fund which is constituted under the law of contract, the constitution or articles that define the fund. These are embodied in a Contract.

## Relationships

- **Subclass of**: [Constitution](/concepts/fibo/FND/Law/LegalCore/Constitution.md)

## Annotations

- **label** (en): fund legal form documentation
- **definition** (en): For a fund which is constituted under the law of contract, the constitution or articles that define the fund. These are embodied in a Contract.
- **explanatoryNote** (en): From ISO FIBIM "Umbrella Fund" narrative: In securities, a collective investment scheme that has a contractual or a corporate form. When it has a contractual form, a fund is constituted under either the law of contract or under the trust law and thus it is not a legal entity. In its corporate form, a fund is a legal entity and is structured as a company.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
