---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: US Treasury bill auction date rule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rule for setting auction dates for US Treasury bills
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.treasurydirect.gov/instit/auctfund/work/work.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: To finance the public debt, the U.S. Treasury sells bills, notes, bonds, Floating Rate Notes (FRNs), and Treasury
      Inflation-Protected Securities (TIPS) to institutional and individual investors through public auctions. Treasury auctions
      occur regularly and have a set schedule. Rules and other information are available via announcements of pending auctions.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention
    value: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayFollowing
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/ParametricSchedules/AuctionDateRule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/AuctionDateRule
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/USTreasuryBillAuctionDateRule
sources:
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: US Treasury bill auction date rule
type: Ontology Class
---

# US Treasury bill auction date rule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/USTreasuryBillAuctionDateRule>

## Definition

rule for setting auction dates for US Treasury bills

## Relationships

- **Subclass of**: [AuctionDateRule](/concepts/fibo/SEC/Securities/ParametricSchedules/AuctionDateRule.md)

## Constraints

- **[hasBusinessDayConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayFollowing`

## Annotations

- **label**: US Treasury bill auction date rule
- **definition**: rule for setting auction dates for US Treasury bills
- **adaptedFrom**: https://www.treasurydirect.gov/instit/auctfund/work/work.htm
- **explanatoryNote**: To finance the public debt, the U.S. Treasury sells bills, notes, bonds, Floating Rate Notes (FRNs), and Treasury Inflation-Protected Securities (TIPS) to institutional and individual investors through public auctions. Treasury auctions occur regularly and have a set schedule. Rules and other information are available via announcements of pending auctions.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
