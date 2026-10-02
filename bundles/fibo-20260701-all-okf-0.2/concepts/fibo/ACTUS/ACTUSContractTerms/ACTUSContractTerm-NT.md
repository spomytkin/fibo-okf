---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - NT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterMapping
    value: Starting from the contract or leg 1 of a swap, fibo-fnd-acc-cur:hasNotionalAmount fibo-fnd-acc-cur:MonetaryAmount;
      fibo-fnd-acc-cur:hasAmount xsd:decimal
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: notionalPrincipal
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "Current nominal value of the contract. For debt instrument this is the current remaining notional outstanding.\
      \ \n\nNT is generally the basis on which interest payments are calculated. If IPCBS is set, IPCBS may introduce a different\
      \ basis for interest payment calculation."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: NT
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Notional Principal
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-NT
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - NT
type: Ontology Individual
---

# ACTUS contract term - NT

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-NT>

## Relationships

- **Related to**: [ACTUSContractTermGroup-NotionalPrincipal](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md)

## Annotations

- **label**: ACTUS contract term - NT
- **hasParameterMapping**: Starting from the contract or leg 1 of a swap, fibo-fnd-acc-cur:hasNotionalAmount fibo-fnd-acc-cur:MonetaryAmount; fibo-fnd-acc-cur:hasAmount xsd:decimal
- **hasParameterName**: notionalPrincipal
- **hasDescription**: Current nominal value of the contract. For debt instrument this is the current remaining notional outstanding.   NT is generally the basis on which interest payments are calculated. If IPCBS is set, IPCBS may introduce a different basis for interest payment calculation.
- **hasTag**: NT
- **hasTextualName**: Notional Principal

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
