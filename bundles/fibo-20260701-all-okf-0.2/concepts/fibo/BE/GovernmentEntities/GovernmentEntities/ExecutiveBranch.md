---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: executive branch
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the branch of government that is authorized and responsible for the daily administration of the government
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.usa.gov/branches-of-government
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The executive branch executes and enforces the law.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/BranchOfGovernment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/BranchOfGovernment
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/ExecutiveBranch
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: executive branch
type: Ontology Class
---

# executive branch

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/ExecutiveBranch>

## Definition

the branch of government that is authorized and responsible for the daily administration of the government

## Relationships

- **Subclass of**: [BranchOfGovernment](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/BranchOfGovernment.md)

## Annotations

- **label**: executive branch
- **definition**: the branch of government that is authorized and responsible for the daily administration of the government
- **adaptedFrom**: https://www.usa.gov/branches-of-government
- **explanatoryNote**: The executive branch executes and enforces the law.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
