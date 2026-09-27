---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: regulates supply of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a regulatory agency to something it controls or supervises the availability of in some market by means
      of rules and regulations
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: The Federal Reserve System, whose banks together comprise the central bank of the United States, supervises banking
      system and regulates the money supply in the US.
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/regulatesSupplyOf
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: regulates supply of
type: Ontology Property
---

# regulates supply of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/regulatesSupplyOf>

## Definition

relates a regulatory agency to something it controls or supervises the availability of in some market by means of rules and regulations

## Relationships

- **Domain**: [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)
- **Subproperty of**: [governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)

## Annotations

- **label**: regulates supply of
- **definition**: relates a regulatory agency to something it controls or supervises the availability of in some market by means of rules and regulations
- **example**: The Federal Reserve System, whose banks together comprise the central bank of the United States, supervises banking system and regulates the money supply in the US.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
