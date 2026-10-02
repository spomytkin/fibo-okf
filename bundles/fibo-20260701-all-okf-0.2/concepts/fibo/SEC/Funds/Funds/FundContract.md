---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund contract
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract that embodies and defines the fund legal form in cases where there is no independent organization
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'From ISO FIBIM "Umbrella Fund" narrative: In securities, a collective investment scheme that has a contractual
      or a corporate form. When it has a contractual form, a fund is constituted under either the law of contract or under
      the trust law and thus it is not a legal entity. In its corporate form, a fund is a legal entity and is structured as
      a company.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundLegalFormDocumentation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundContract
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: fund contract
type: Ontology Class
---

# fund contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundContract>

## Definition

contract that embodies and defines the fund legal form in cases where there is no independent organization

## Relationships

- **Subclass of**: [OrganizationCoveringAgreement](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement.md)

## Constraints

- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: some values from of type [FundLegalFormDocumentation](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundLegalFormDocumentation.md)

## Annotations

- **label** (en): fund contract
- **definition** (en): contract that embodies and defines the fund legal form in cases where there is no independent organization
- **explanatoryNote** (en): From ISO FIBIM "Umbrella Fund" narrative: In securities, a collective investment scheme that has a contractual or a corporate form. When it has a contractual form, a fund is constituted under either the law of contract or under the trust law and thus it is not a legal entity. In its corporate form, a fund is a legal entity and is structured as a company.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
