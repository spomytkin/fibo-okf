---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: HMDA report
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a report prepared to satisfy HMDA regulatory reporting requirements as described US section 1003.3(c) of the Revised
      Home Mortgage Disclosure Act of 2015
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: The filter class on the hasReportingAgent restriction comes from the hasIdentity restriction on FinancialServiceProvider,
      which, unfortunately, is a PartyInRole.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: the Revised HMDA regulatory text.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isSubmittedBy
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isSubmittedTo
  - filler: http://www.w3.org/2001/XMLSchema#positiveInteger
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasNumberOfEntries
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Reporting/Report.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report
sources:
- id: fibo-source-c6feed0cf8
  resource: references/fibo/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.rdf
  sha256: c6feed0cf8f9c31063c105e293abb9e2add43152d3993dd5c4e7722d89df3473
  title: FIBO source LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.rdf
title: HMDA report
type: Ontology Class
---

# HMDA report

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report>

## Definition

a report prepared to satisfy HMDA regulatory reporting requirements as described US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015

## Relationships

- **Subclass of**: [Report](/concepts/fibo/FND/Arrangements/Reporting/Report.md)

## Constraints

- **[isSubmittedBy](/concepts/fibo/FND/Arrangements/Reporting/isSubmittedBy.md)**: min qualified cardinality 0
- **[isSubmittedTo](/concepts/fibo/FND/Arrangements/Reporting/isSubmittedTo.md)**: some values from of type [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)
- **[hasNumberOfEntries](/concepts/fibo/FND/Utilities/Analytics/hasNumberOfEntries.md)**: some values from of type [positiveInteger](<http://www.w3.org/2001/XMLSchema#positiveInteger>)

## Annotations

- **label**: HMDA report
- **definition**: a report prepared to satisfy HMDA regulatory reporting requirements as described US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015
- **editorialNote**: The filter class on the hasReportingAgent restriction comes from the hasIdentity restriction on FinancialServiceProvider, which, unfortunately, is a PartyInRole.
- **adaptedFrom**: the Revised HMDA regulatory text.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
