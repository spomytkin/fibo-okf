---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: reporting party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party providing a report, typically in response to some contractual, legal, regulatory or other business requirement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/provides
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/ReportingParty
sources:
- id: fibo-source-a52060e8b1
  resource: references/fibo/FND/Arrangements/Reporting.rdf
  sha256: a52060e8b187a3f08302027cf7c7be15c9b644d9a3a7105f69a6415913db5143
  title: FIBO source FND/Arrangements/Reporting.rdf
title: reporting party
type: Ontology Class
---

# reporting party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/ReportingParty>

## Definition

party providing a report, typically in response to some contractual, legal, regulatory or other business requirement

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: some values from of type [Report](/concepts/fibo/FND/Arrangements/Reporting/Report.md)

## Annotations

- **label**: reporting party
- **definition**: party providing a report, typically in response to some contractual, legal, regulatory or other business requirement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
