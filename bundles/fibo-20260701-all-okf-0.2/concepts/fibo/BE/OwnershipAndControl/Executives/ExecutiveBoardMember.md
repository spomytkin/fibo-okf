---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: executive board member
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: member of a board of directors that is also an employee of the organization
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: inside director
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/BoardMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMember
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ExecutiveBoardMember
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: executive board member
type: Ontology Class
---

# executive board member

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ExecutiveBoardMember>

## Definition

member of a board of directors that is also an employee of the organization

## Relationships

- **Subclass of**: [BoardMember](/concepts/fibo/BE/OwnershipAndControl/Executives/BoardMember.md)
- **Subclass of**: [Employee](/concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md)

## Annotations

- **label**: executive board member
- **definition**: member of a board of directors that is also an employee of the organization
- **synonym**: inside director

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
