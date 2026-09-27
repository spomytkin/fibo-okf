---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has final maturity date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the final payment date of a financial instrument, at which point the principal (and all remaining interest)
      is due to be paid
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasFinalMaturityDate
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has final maturity date
type: Ontology Property
---

# has final maturity date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasFinalMaturityDate>

## Definition

indicates the final payment date of a financial instrument, at which point the principal (and all remaining interest) is due to be paid

## Relationships

- **Domain**: [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label**: has final maturity date
- **definition**: indicates the final payment date of a financial instrument, at which point the principal (and all remaining interest) is due to be paid

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
