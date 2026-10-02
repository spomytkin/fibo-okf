---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal form change
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action indicating a modification of the legal form of the organization
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: In the United States it is common for companies established as Subchapter S Corporations (S-Corp), typically early
      stage companies, to modify their structure to become full-fledged Subchapter C Corporations (C-Corp) to facilitate outside
      fundraising, mergers, acquisitions, and public offerings. Other common form changes include migration from sole proprietorships
      to more formally registered organizations (e.g., LLC, S-Corp, C-Corp, etc.)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/LegalFormChange
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: legal form change
type: Ontology Class
---

# legal form change

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/LegalFormChange>

## Definition

corporate action indicating a modification of the legal form of the organization

## Relationships

- **Subclass of**: [MandatoryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)

## Annotations

- **label** (en): legal form change
- **definition** (en): corporate action indicating a modification of the legal form of the organization
- **example** (en): In the United States it is common for companies established as Subchapter S Corporations (S-Corp), typically early stage companies, to modify their structure to become full-fledged Subchapter C Corporations (C-Corp) to facilitate outside fundraising, mergers, acquisitions, and public offerings. Other common form changes include migration from sole proprietorships to more formally registered organizations (e.g., LLC, S-Corp, C-Corp, etc.)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
