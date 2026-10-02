---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issued security issue information
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'FIBIM: "Elements relating to issue preparation/bringing to market (also known as primary market or Initial Public
      Offering (IPO) issuance) through to issue date."'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Information about the Issuance of a Security, which is maintained throughout the life of the Security.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/hasPartiallyPaidIssuanceSchedule
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/isAbout
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Document
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: issued security issue information
type: Ontology Class
---

# issued security issue information

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation>

## Definition

FIBIM: "Elements relating to issue preparation/bringing to market (also known as primary market or Initial Public Offering (IPO) issuance) through to issue date."

## Additional definitions

- Information about the Issuance of a Security, which is maintained throughout the life of the Security.

## Relationships

- **Subclass of**: [Document](<https://www.omg.org/spec/Commons/Documents/Document>)

## Constraints

- **[hasPartiallyPaidIssuanceSchedule](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/hasPartiallyPaidIssuanceSchedule.md)**: all values from of type [PaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
- **[isAbout](<https://www.omg.org/spec/Commons/Documents/isAbout>)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label** (en): issued security issue information
- **definition** (en): FIBIM: "Elements relating to issue preparation/bringing to market (also known as primary market or Initial Public Offering (IPO) issuance) through to issue date."
- **definition** (en): Information about the Issuance of a Security, which is maintained throughout the life of the Security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
