---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - PPRD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterMapping
    value: Starting from the contract, fibo-fnd-oac-own:hasAcquisitionPrice fibo-fnd-acc-cur:MonetaryPrice; fibo-fnd-acc-cur:hasAmount
      xsd:decimal
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: priceAtPurchaseDate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "Purchase price exchanged at PRD. \n\nPPRD represents a clean price (includes premium/discount but not IPAC)."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: PPRD
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Price At Purchase Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PPRD
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - PPRD
type: Ontology Individual
---

# ACTUS contract term - PPRD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PPRD>

## Relationships

- **Related to**: [ACTUSContractTermGroup-NotionalPrincipal](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md)

## Annotations

- **label**: ACTUS contract term - PPRD
- **hasParameterMapping**: Starting from the contract, fibo-fnd-oac-own:hasAcquisitionPrice fibo-fnd-acc-cur:MonetaryPrice; fibo-fnd-acc-cur:hasAmount xsd:decimal
- **hasParameterName**: priceAtPurchaseDate
- **hasDescription**: Purchase price exchanged at PRD.   PPRD represents a clean price (includes premium/discount but not IPAC).
- **hasTag**: PPRD
- **hasTextualName**: Price At Purchase Date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
