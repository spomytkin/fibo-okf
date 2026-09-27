---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: submitter
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party presenting something, such as a regulatory report
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/submits
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Submitter
sources:
- id: fibo-source-a52060e8b1
  resource: references/fibo/FND/Arrangements/Reporting.rdf
  sha256: a52060e8b187a3f08302027cf7c7be15c9b644d9a3a7105f69a6415913db5143
  title: FIBO source FND/Arrangements/Reporting.rdf
title: submitter
type: Ontology Class
---

# submitter

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Submitter>

## Definition

party presenting something, such as a regulatory report

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[submits](/concepts/fibo/FND/Arrangements/Reporting/submits.md)**: some values from of type [Report](/concepts/fibo/FND/Arrangements/Reporting/Report.md)

## Annotations

- **label**: submitter
- **definition**: party presenting something, such as a regulatory report

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
