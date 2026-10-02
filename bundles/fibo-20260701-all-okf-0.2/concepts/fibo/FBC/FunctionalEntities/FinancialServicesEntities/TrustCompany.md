---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trust company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution that acts as a fiduciary, trustee or agent of trusts and agencies
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A professional trust company may be independently owned or owned by, for example, a bank or a law firm, and which
      specializes in being a trustee of various kinds of trusts. The trust company oversees the management of assets covered
      by the trust agreement. Such companies often are used when a grantor feels the trust company can do an equal or better
      job managing the assets than an individual person, or if the grantor does not know of anyone else who can act as trustee.
      Trust companies sometimes act as fiscal agents for corporations by attending to the registration and transfer of their
      stocks and bonds, serving as a trustee for their bond and mortgage creditors, and transacting general banking and loan
      business.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/TrustCompany
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: trust company
type: Ontology Class
---

# trust company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/TrustCompany>

## Definition

financial institution that acts as a fiduciary, trustee or agent of trusts and agencies

## Relationships

- **Subclass of**: [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [Corporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md)

## Annotations

- **label**: trust company
- **definition**: financial institution that acts as a fiduciary, trustee or agent of trusts and agencies
- **explanatoryNote**: A professional trust company may be independently owned or owned by, for example, a bank or a law firm, and which specializes in being a trustee of various kinds of trusts. The trust company oversees the management of assets covered by the trust agreement. Such companies often are used when a grantor feels the trust company can do an equal or better job managing the assets than an individual person, or if the grantor does not know of anyone else who can act as trustee. Trust companies sometimes act as fiscal agents for corporations by attending to the registration and transfer of their stocks and bonds, serving as a trustee for their bond and mortgage creditors, and transacting general banking and loan business.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
