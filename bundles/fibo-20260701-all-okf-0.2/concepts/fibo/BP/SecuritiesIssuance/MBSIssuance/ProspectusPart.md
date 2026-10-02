---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: prospectus part
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A part or section of a prospectus for a securities issue.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This may for example be a termsheet, information about tranche breakdown and so on. These are defined as separate
      information entities in as far as each of these has some specific individual relationship to some other information
      deliverable, such as a draft of each part which is defined in separate process activities but becomes part of the whole
      prospectus. Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MBSIssuance/ProspectusPart
sources:
- id: fibo-source-98ae1fbc1c
  resource: references/fibo/BP/SecuritiesIssuance/MBSIssuance.rdf
  sha256: 98ae1fbc1c6325c22ec32be6fe2c3b1c11bf20f64ae80d0087c27a7f332d20f1
  title: FIBO source BP/SecuritiesIssuance/MBSIssuance.rdf
title: prospectus part
type: Ontology Class
---

# prospectus part

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MBSIssuance/ProspectusPart>

## Definition

A part or section of a prospectus for a securities issue.

## Relationships

- **Subclass of**: [ContractualElement](/concepts/fibo/FND/Agreements/Contracts/ContractualElement.md)

## Annotations

- **label**: prospectus part
- **definition**: A part or section of a prospectus for a securities issue.
- **explanatoryNote**: This may for example be a termsheet, information about tranche breakdown and so on. These are defined as separate information entities in as far as each of these has some specific individual relationship to some other information deliverable, such as a draft of each part which is defined in separate process activities but becomes part of the whole prospectus. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
