---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CURS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterMapping
    value: Starting from the contract, (1) fibo-fbc-fi-stl:hasPreferredSettlementCurrency fibo-fnd-acc-cur:Currency; cmns-dsg:isSignifiedBy
      fibo-fnd-acc-cur:CurrencyIdentifier; cmns-dsg;hasTag xsd:string
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: settlementCurrency
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'The currency in which cash flows are settled. This currency can be different from the currency (CUR) in which
      cash flows or the contract, respectively, is denominated in which case the respective FX-rate applies at settlement
      time.


      If no settlement currency is defined the cash flows are settled in the currency in which they are denominated.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: CURS
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Settlement Currency
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CURS
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CURS
type: Ontology Individual
---

# ACTUS contract term - CURS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CURS>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Settlement](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement.md)

## Annotations

- **label**: ACTUS contract term - CURS
- **hasParameterMapping**: Starting from the contract, (1) fibo-fbc-fi-stl:hasPreferredSettlementCurrency fibo-fnd-acc-cur:Currency; cmns-dsg:isSignifiedBy fibo-fnd-acc-cur:CurrencyIdentifier; cmns-dsg;hasTag xsd:string
- **hasParameterName**: settlementCurrency
- **hasDescription**: The currency in which cash flows are settled. This currency can be different from the currency (CUR) in which cash flows or the contract, respectively, is denominated in which case the respective FX-rate applies at settlement time.  If no settlement currency is defined the cash flows are settled in the currency in which they are denominated.
- **hasTag**: CURS
- **hasTextualName**: Settlement Currency

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
