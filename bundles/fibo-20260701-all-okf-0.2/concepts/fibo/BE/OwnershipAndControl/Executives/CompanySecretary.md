---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: company secretary
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate officer appointed by the directors of an organization, responsible for ensuring compliance with legal
      obligations related to corporate governance
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: His or her formal duties include (1) calling meetings, (2) recording minutes of the meetings, (3) keeping statutory
      record books, (4) proper payment of dividend and interest payments, and (5) proper drafting and execution of agreements,
      contracts, and resolutions.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: corporate secretary
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/CorporateOfficer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CorporateOfficer
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CompanySecretary
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: company secretary
type: Ontology Class
---

# company secretary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CompanySecretary>

## Definition

corporate officer appointed by the directors of an organization, responsible for ensuring compliance with legal obligations related to corporate governance

## Relationships

- **Subclass of**: [CorporateOfficer](/concepts/fibo/BE/OwnershipAndControl/Executives/CorporateOfficer.md)

## Annotations

- **label**: company secretary
- **definition**: corporate officer appointed by the directors of an organization, responsible for ensuring compliance with legal obligations related to corporate governance
- **explanatoryNote**: His or her formal duties include (1) calling meetings, (2) recording minutes of the meetings, (3) keeping statutory record books, (4) proper payment of dividend and interest payments, and (5) proper drafting and execution of agreements, contracts, and resolutions.
- **synonym**: corporate secretary

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
