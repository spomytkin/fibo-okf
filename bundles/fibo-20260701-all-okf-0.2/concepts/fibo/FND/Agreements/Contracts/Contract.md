---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: voluntary, deliberate agreement between competent parties to which the parties agree to be legally bound, and for
      which the parties provide valuable consideration
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A contractual relationship is evidenced by (1) an offer, (2) acceptance of the offer, and a (3) valid (legal and
      valuable) consideration. A contract is a kind of agreement, and as such it embodies the assertion that it has been negotiated,
      such negotiation having included the presence of some offer and the acceptance of that offer on the part of either or
      both of the parties.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Contracts are usually written but may be spoken or implied, and generally have to do with employment, sale or lease,
      or tenancy.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the data of issuance may be, but is not always, the same as the effective date.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualElement
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasEffectiveDate
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Agreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: contract
type: Ontology Class
---

# contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract>

## Definition

voluntary, deliberate agreement between competent parties to which the parties agree to be legally bound, and for which the parties provide valuable consideration

## Relationships

- **Subclass of**: [Agreement](/concepts/fibo/FND/Agreements/Agreements/Agreement.md)

## Constraints

- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: min qualified cardinality 2 of type [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [ContractualElement](/concepts/fibo/FND/Agreements/Contracts/ContractualElement.md)
- **[hasEffectiveDate](/concepts/fibo/FND/Agreements/Contracts/hasEffectiveDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label**: contract
- **definition**: voluntary, deliberate agreement between competent parties to which the parties agree to be legally bound, and for which the parties provide valuable consideration
- **explanatoryNote**: A contractual relationship is evidenced by (1) an offer, (2) acceptance of the offer, and a (3) valid (legal and valuable) consideration. A contract is a kind of agreement, and as such it embodies the assertion that it has been negotiated, such negotiation having included the presence of some offer and the acceptance of that offer on the part of either or both of the parties.
- **explanatoryNote**: Contracts are usually written but may be spoken or implied, and generally have to do with employment, sale or lease, or tenancy.
- **explanatoryNote**: Note that the data of issuance may be, but is not always, the same as the effective date.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
