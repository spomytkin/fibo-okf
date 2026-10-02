---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - PTD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterMapping
    value: Starting from the contract, fibo-ind-fx-fx:hasQuotedExchangeRate fibo-ind-fx-fx:QuotedExchangeRate; fibo-fnd-acc-cur:hasRateValue
      xsd:decimal
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: priceAtTerminationDate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Sellingprice exchanged at PTD PTDrepresents a clean price (includes premium/discount but not IPAC
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: PTD
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Price At Termination Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PTD
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - PTD
type: Ontology Individual
---

# ACTUS contract term - PTD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PTD>

## Relationships

- **Related to**: [ACTUSContractTermGroup-NotionalPrincipal](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md)

## Annotations

- **label**: ACTUS contract term - PTD
- **hasParameterMapping**: Starting from the contract, fibo-ind-fx-fx:hasQuotedExchangeRate fibo-ind-fx-fx:QuotedExchangeRate; fibo-fnd-acc-cur:hasRateValue xsd:decimal
- **hasParameterName**: priceAtTerminationDate
- **hasDescription**: Sellingprice exchanged at PTD PTDrepresents a clean price (includes premium/discount but not IPAC
- **hasTag**: PTD
- **hasTextualName**: Price At Termination Date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
