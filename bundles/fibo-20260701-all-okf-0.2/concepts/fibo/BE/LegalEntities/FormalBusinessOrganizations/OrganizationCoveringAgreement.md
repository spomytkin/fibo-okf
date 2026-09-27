---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: organization covering agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract between the principals in a formal organization that specifies the relationship between the principals,
      and between the principals and the entity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Also covers the aims and purposes of the Entity.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement
sources:
- id: fibo-source-9758af6c79
  resource: references/fibo/BE/LegalEntities/FormalBusinessOrganizations.rdf
  sha256: 9758af6c796f157eedb21d72cde0822cb7a2ecbd6b5a70ef23be48121c598ede
  title: FIBO source BE/LegalEntities/FormalBusinessOrganizations.rdf
title: organization covering agreement
type: Ontology Class
---

# organization covering agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement>

## Definition

contract between the principals in a formal organization that specifies the relationship between the principals, and between the principals and the entity

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Annotations

- **label**: organization covering agreement
- **definition**: contract between the principals in a formal organization that specifies the relationship between the principals, and between the principals and the entity
- **explanatoryNote**: Also covers the aims and purposes of the Entity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
