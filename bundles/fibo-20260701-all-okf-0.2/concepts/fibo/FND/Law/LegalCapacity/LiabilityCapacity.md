---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: liability capacity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the ability to be sued at law
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Note that for the purposes of this model, this is distinct from culpability (the ability to commit criminal acts).
      That would be a separate and analogous term but with grounding in criminal rather than civil law.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalCapacity
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LiabilityCapacity
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: liability capacity
type: Ontology Class
---

# liability capacity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LiabilityCapacity>

## Definition

the ability to be sued at law

## Relationships

- **Subclass of**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md)

## Annotations

- **label** (en): liability capacity
- **definition**: the ability to be sued at law
- **editorialNote**: Note that for the purposes of this model, this is distinct from culpability (the ability to commit criminal acts). That would be a separate and analogous term but with grounding in criminal rather than civil law.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
