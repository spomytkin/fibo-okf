---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: novation netting provision
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contractual element that specifies what should be done with respect to netting when a given contract is replaced
      with another
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Novation netting contemplates that for each value date and for each currency, the parties agree that all existing
      contracts will be canceled (discharged and extinguished) and simultaneously replaced by a new contract that aggregates
      and nets all of the payment obligations of the original contracts. Novation netting occurs immediately when a nettable
      transaction is entered into.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/NettingProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NettingProvision
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NovationNettingProvision
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: novation netting provision
type: Ontology Class
---

# novation netting provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NovationNettingProvision>

## Definition

contractual element that specifies what should be done with respect to netting when a given contract is replaced with another

## Relationships

- **Subclass of**: [NettingProvision](/concepts/fibo/FND/Agreements/Contracts/NettingProvision.md)

## Annotations

- **label** (en): novation netting provision
- **definition** (en): contractual element that specifies what should be done with respect to netting when a given contract is replaced with another
- **explanatoryNote**: Novation netting contemplates that for each value date and for each currency, the parties agree that all existing contracts will be canceled (discharged and extinguished) and simultaneously replaced by a new contract that aggregates and nets all of the payment obligations of the original contracts. Novation netting occurs immediately when a nettable transaction is entered into.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
