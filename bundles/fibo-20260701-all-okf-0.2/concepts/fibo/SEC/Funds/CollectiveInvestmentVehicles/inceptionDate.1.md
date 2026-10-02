---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: inception date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'Authorization date in the country of origin. Further Notes See definition in Inception Date for Fund. Separate
      fact exists here. Same definition used. EFAMA Review notes: Inception Date exists as soon as there is a prospectus,
      so it is a fact about a Share Class even if the share class is never formally issued or offered to the public. Legal
      structure exists even if something is not launched. Editor question: Review stated this was a fact about Share Class;
      confirm this fact does not apply to Bond and Note units, or was the term Share Class being used to mean all three? Meanwhile
      I have put the term "Issue Date" as a fact about all Fund Unit, as this is given a sa separate term in the EFAMA DD
      spreadsheet. MAy come clearer in the next version of that.'
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/inceptionDate.1
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: inception date
type: Ontology Property
---

# inception date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/inceptionDate.1>

## Definition

Authorization date in the country of origin. Further Notes See definition in Inception Date for Fund. Separate fact exists here. Same definition used. EFAMA Review notes: Inception Date exists as soon as there is a prospectus, so it is a fact about a Share Class even if the share class is never formally issued or offered to the public. Legal structure exists even if something is not launched. Editor question: Review stated this was a fact about Share Class; confirm this fact does not apply to Bond and Note units, or was the term Share Class being used to mean all three? Meanwhile I have put the term "Issue Date" as a fact about all Fund Unit, as this is given a sa separate term in the EFAMA DD spreadsheet. MAy come clearer in the next version of that.

## Relationships

- **Domain**: [FundShareClassUnit](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit.md)
- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label** (en): inception date
- **definition** (en): Authorization date in the country of origin. Further Notes See definition in Inception Date for Fund. Separate fact exists here. Same definition used. EFAMA Review notes: Inception Date exists as soon as there is a prospectus, so it is a fact about a Share Class even if the share class is never formally issued or offered to the public. Legal structure exists even if something is not launched. Editor question: Review stated this was a fact about Share Class; confirm this fact does not apply to Bond and Note units, or was the term Share Class being used to mean all three? Meanwhile I have put the term "Issue Date" as a fact about all Fund Unit, as this is given a sa separate term in the EFAMA DD spreadsheet. MAy come clearer in the next version of that.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
