---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: condition precedent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: stipulation that specifies conditions that must be met before some aspect of a contract takes effect
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Condition precedents are common in wills and trusts. They include events or states of affairs that act as triggers
      for the contract to come into effect, such as a beneficiary reaching the age of maturity, or death of a trustor, as
      well as define obligations on a party to the contract, such as those required of a trustee on the death of a trustor.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There may also be condition precedents in the ongoing life of a contract, which state that if condition X occurs,
      event Y will then occur. Condition X is the condition precedent.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isPredicatedOn
    value: N3d2a3793b34b4f348e0e09738373cada
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ConditionPrecedent
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: condition precedent
type: Ontology Class
---

# condition precedent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ConditionPrecedent>

## Definition

stipulation that specifies conditions that must be met before some aspect of a contract takes effect

## Relationships

- **Subclass of**: [ContractualElement](/concepts/fibo/FND/Agreements/Contracts/ContractualElement.md)

## Constraints

- **[isPredicatedOn](/concepts/fibo/FND/Law/LegalCapacity/isPredicatedOn.md)**: some values from value `N3d2a3793b34b4f348e0e09738373cada`

## Annotations

- **label**: condition precedent
- **definition**: stipulation that specifies conditions that must be met before some aspect of a contract takes effect
- **explanatoryNote**: Condition precedents are common in wills and trusts. They include events or states of affairs that act as triggers for the contract to come into effect, such as a beneficiary reaching the age of maturity, or death of a trustor, as well as define obligations on a party to the contract, such as those required of a trustee on the death of a trustor.
- **explanatoryNote**: There may also be condition precedents in the ongoing life of a contract, which state that if condition X occurs, event Y will then occur. Condition X is the condition precedent.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
