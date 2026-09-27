---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual commitment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: provision specifying something that the contracting parties agree to, i.e., a promise or pledge made by one of
      the parties to perform some action or fulfill some duty
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: Contractual commitments include general conditions which are common to all types of contracts, such as general
      and special arrangements, provisions, requirements, rules, rights and obligations, specifications, and standards that
      form an integral part of an agreement or contract, as well as special conditions which are peculiar to a specific contract
      (such as, contract change conditions, payment conditions, price variation clauses, penalties). Such a commitment indicates
      an intention or willingness to do something, which may not be legally binding, for example, to negotiate in good faith.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isMandatedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasPart
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: contractual commitment
type: Ontology Class
---

# contractual commitment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment>

## Definition

provision specifying something that the contracting parties agree to, i.e., a promise or pledge made by one of the parties to perform some action or fulfill some duty

## Relationships

- **Subclass of**: [ContractualElement](/concepts/fibo/FND/Agreements/Contracts/ContractualElement.md)

## Constraints

- **[isMandatedBy](/concepts/fibo/FND/Relations/Relations/isMandatedBy.md)**: some values from of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)
- **[hasPart](<https://www.omg.org/spec/Commons/Collections/hasPart>)**: all values from of type [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Annotations

- **label**: contractual commitment
- **definition**: provision specifying something that the contracting parties agree to, i.e., a promise or pledge made by one of the parties to perform some action or fulfill some duty
- **scopeNote**: Contractual commitments include general conditions which are common to all types of contracts, such as general and special arrangements, provisions, requirements, rules, rights and obligations, specifications, and standards that form an integral part of an agreement or contract, as well as special conditions which are peculiar to a specific contract (such as, contract change conditions, payment conditions, price variation clauses, penalties). Such a commitment indicates an intention or willingness to do something, which may not be legally binding, for example, to negotiate in good faith.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
