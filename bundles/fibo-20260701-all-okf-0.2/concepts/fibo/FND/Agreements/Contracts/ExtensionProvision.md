---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: extension provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms that specify the conditions under which a contract can be extended
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the case of a debt instrument, an extension may include extending the time allowed for repayment of the principal,
      the maturity date, and so forth.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasExtendablePeriod
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ExtensionProvision
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: extension provision
type: Ontology Class
---

# extension provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ExtensionProvision>

## Definition

contract terms that specify the conditions under which a contract can be extended

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Constraints

- **[hasExtendablePeriod](/concepts/fibo/FND/Agreements/Contracts/hasExtendablePeriod.md)**: min qualified cardinality 0 of type [ExplicitDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod>)

## Annotations

- **label**: extension provision
- **definition**: contract terms that specify the conditions under which a contract can be extended
- **explanatoryNote**: In the case of a debt instrument, an extension may include extending the time allowed for repayment of the principal, the maturity date, and so forth.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
