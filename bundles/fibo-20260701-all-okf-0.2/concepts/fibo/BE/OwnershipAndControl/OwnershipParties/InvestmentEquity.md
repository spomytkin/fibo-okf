---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investment equity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: equity that represents an ownership interest in some entity, but may or may not take the form of shareholders's
      equity
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Typically an investment in some entity may take the form of shares (issued or privately held), i.e., shareholders'
      equity, or it may take the form of some capital amount which is not reflected in shareholders' equity. In each case,
      there would typically be a contractual basis for the investment setting out what controls or other benefits accrue to
      the investor.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/Investor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/OwnersEquity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/OwnersEquity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: investment equity
type: Ontology Class
---

# investment equity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity>

## Definition

equity that represents an ownership interest in some entity, but may or may not take the form of shareholders's equity

## Relationships

- **Subclass of**: [OwnersEquity](/concepts/fibo/FND/OwnershipAndControl/Ownership/OwnersEquity.md)

## Constraints

- **[isHeldBy](/concepts/fibo/FND/Relations/Relations/isHeldBy.md)**: some values from of type [Investor](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md)

## Annotations

- **label**: investment equity
- **definition**: equity that represents an ownership interest in some entity, but may or may not take the form of shareholders's equity
- **editorialNote**: Typically an investment in some entity may take the form of shares (issued or privately held), i.e., shareholders' equity, or it may take the form of some capital amount which is not reflected in shareholders' equity. In each case, there would typically be a contractual basis for the investment setting out what controls or other benefits accrue to the investor.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
