---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: company law
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legislation under which the formation, registration or incorporation, governance, and dissolution of a firm is
      administered and controlled
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: corporate law
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCore/StatuteLaw.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/StatuteLaw
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CompanyLaw
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: company law
type: Ontology Class
---

# company law

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CompanyLaw>

## Definition

legislation under which the formation, registration or incorporation, governance, and dissolution of a firm is administered and controlled

## Relationships

- **Subclass of**: [StatuteLaw](/concepts/fibo/FND/Law/LegalCore/StatuteLaw.md)

## Annotations

- **label**: company law
- **definition**: legislation under which the formation, registration or incorporation, governance, and dissolution of a firm is administered and controlled
- **synonym**: corporate law

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
