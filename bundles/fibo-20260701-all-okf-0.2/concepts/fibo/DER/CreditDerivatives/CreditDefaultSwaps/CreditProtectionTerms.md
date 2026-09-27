---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit protection terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal terms that define triggering events and associated conditions related to settlement
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that there may be additional payment schedules or a more complex calculation formula required depending on
      the terms of the contract.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: contingent leg
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/allowsSubstitution
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/hasScheduledTerminationDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligationBuyer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasBuyer
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligationSeller
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasSeller
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/specifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: credit protection terms
type: Ontology Class
---

# credit protection terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms>

## Definition

legal terms that define triggering events and associated conditions related to settlement

## Relationships

- **Subclass of**: [DerivativeTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)

## Constraints

- **[allowsSubstitution](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/allowsSubstitution.md)**: min qualified cardinality 0 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[hasScheduledTerminationDate](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/hasScheduledTerminationDate.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasBuyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/hasBuyer.md)**: some values from of type [DeliverableObligationBuyer](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligationBuyer.md)
- **[hasSeller](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/hasSeller.md)**: some values from of type [DeliverableObligationSeller](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligationSeller.md)
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: some values from of type [DeliverableObligation](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation.md)
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: some values from of type [TriggeringEvent](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md)

## Annotations

- **label** (en): credit protection terms
- **definition** (en): legal terms that define triggering events and associated conditions related to settlement
- **explanatoryNote** (en): Note that there may be additional payment schedules or a more complex calculation formula required depending on the terms of the contract.
- **synonym** (en): contingent leg

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
