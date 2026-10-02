---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: internal auditor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: employee who is qualified and authorized to review and verify the accuracy of financial records and evaluate internal
      controls and compliance
  disjoint_with:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/ExternalAuditor.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ExternalAuditor
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/Auditor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Auditor
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/InternalAuditor
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: internal auditor
type: Ontology Class
---

# internal auditor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/InternalAuditor>

## Definition

employee who is qualified and authorized to review and verify the accuracy of financial records and evaluate internal controls and compliance

## Relationships

- **Subclass of**: [Auditor](/concepts/fibo/BE/OwnershipAndControl/Executives/Auditor.md)
- **Subclass of**: [Employee](/concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md)

## Constraints

- **Disjoint with**: [ExternalAuditor](/concepts/fibo/BE/OwnershipAndControl/Executives/ExternalAuditor.md)

## Annotations

- **label**: internal auditor
- **definition**: employee who is qualified and authorized to review and verify the accuracy of financial records and evaluate internal controls and compliance

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
