---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: profit objective
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: objective that reflects pursuit of a financial benefit that may be realized when the amount of revenue gained from
      a business activity exceeds the expenses, costs and taxes needed to sustain that activity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Any profit that is gained goes to the business's owners, who may or may not decide to spend it on the business.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: for profit objective
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: profit motive
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/BusinessObjective.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/BusinessObjective
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/ProfitObjective
sources:
- id: fibo-source-5d6bb270b5
  resource: references/fibo/BE/LegalEntities/LegalPersons.rdf
  sha256: 5d6bb270b50e9a3b5bf8d32aa2448ba56a3e1b9880a137cb89b1bdb2d7811196
  title: FIBO source BE/LegalEntities/LegalPersons.rdf
title: profit objective
type: Ontology Class
---

# profit objective

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/ProfitObjective>

## Definition

objective that reflects pursuit of a financial benefit that may be realized when the amount of revenue gained from a business activity exceeds the expenses, costs and taxes needed to sustain that activity

## Relationships

- **Subclass of**: [BusinessObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/BusinessObjective.md)

## Annotations

- **label**: profit objective
- **definition**: objective that reflects pursuit of a financial benefit that may be realized when the amount of revenue gained from a business activity exceeds the expenses, costs and taxes needed to sustain that activity
- **explanatoryNote**: Any profit that is gained goes to the business's owners, who may or may not decide to spend it on the business.
- **synonym**: for profit objective
- **synonym**: profit motive

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
