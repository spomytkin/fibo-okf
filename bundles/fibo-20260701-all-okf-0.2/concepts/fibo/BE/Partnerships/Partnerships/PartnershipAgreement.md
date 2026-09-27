---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: partnership agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract between partners in a partnership that establishes the terms and conditions of the relationship between
      the partners
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: articles of partnership
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partner
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/PartnershipAgreement
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: partnership agreement
type: Ontology Class
---

# partnership agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/PartnershipAgreement>

## Definition

contract between partners in a partnership that establishes the terms and conditions of the relationship between the partners

## Relationships

- **Subclass of**: [OrganizationCoveringAgreement](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement.md)

## Constraints

- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Partner](/concepts/fibo/BE/Partnerships/Partnerships/Partner.md)

## Annotations

- **label**: partnership agreement
- **definition**: contract between partners in a partnership that establishes the terms and conditions of the relationship between the partners
- **synonym**: articles of partnership

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
