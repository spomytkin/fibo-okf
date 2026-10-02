---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: U.S. bank holding company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bank holding company that is licensed to conduct business in the United States and is regulated and supervised
      by the Federal Reserve in accordance with the Bank Holding Company Act of 1956
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: According to the FFIEC, a bank holding company is a company that owns and/or controls one or more U.S. banks or
      one that owns, or has controlling interest in, one or more banks. A bank holding company may also own another bank holding
      company, which in turn owns or controls a bank; the company at the top of the ownership chain is called the top holder.
      The Board of Governors is responsible for regulating and supervising bank holding companies, even if the bank owned
      by the holding company is under the primary supervision of a different federal agency (OCC or FDIC).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: From the Bank Holding Company Act of 1956, a 'bank holding company' means any company (1) which directly or indirectly
      owns, controls, or holds with power to vote, 25 per centum or more of the voting shares of each of two or more banks
      or of a company which is or becomes a bank holding company by virtue of this Act, or (2) which controls in any manner
      the election of a majority of the directors of each of two or more banks, or (3) for the benefit of whose shareholders
      or members 25 per centum or more of the voting shares of each of two or more banks or a bank holding company is held
      by trustees; and for the purposes of this Act, any successor to any such company shall be deemed to be a bank holding
      company from the date as of which such predecessor company became a bank holding company. Notwithstanding the foregoing,
      (A) no bank shall be a bank holding company by virtue of its ownership or control of shares in a fiduciary capacity,
      except where such shares are held for the benefit of the shareholders of such bank, (B) no company shall be a bank holding
      company which is registered under the Investment Company Act of 1940, and was so registered prior to May 15, 1955 (or
      which is affiliated with any such company in such manner as to constitute an affiliated company within the meaning of
      such Act), unless such company (or such affiliated company), as the case may be, directly owns 25 per centum or more
      of the voting shares of each of two or more banks, (C) no company shall be a bank holding company by virtue of its ownership
      or control of shares acquired by it in connection with its underwriting of securities and which are held only for such
      period of time as will permit the sale thereof upon a reasonable basis, (D) no company formed for the sole purpose of
      participating in a proxy solicitation shall be a bank holding company by virtue of its control of voting rights of shares
      acquired in the course of such solicitation, and (E) no company shall be a bank holding company if at least 80 per centum
      of its total assets are composed of holdings in the field of agriculture.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasPortfolioCompany
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BankHoldingCompany.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BankHoldingCompany
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticEntity
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBankHoldingCompany
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: U.S. bank holding company
type: Ontology Class
---

# U.S. bank holding company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBankHoldingCompany>

## Definition

bank holding company that is licensed to conduct business in the United States and is regulated and supervised by the Federal Reserve in accordance with the Bank Holding Company Act of 1956

## Relationships

- **Subclass of**: [BankHoldingCompany](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BankHoldingCompany.md)
- **Subclass of**: [DomesticEntity](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticEntity.md)

## Constraints

- **[hasPortfolioCompany](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/hasPortfolioCompany.md)**: some values from of type [USBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank.md)

## Annotations

- **label**: U.S. bank holding company
- **definition**: bank holding company that is licensed to conduct business in the United States and is regulated and supervised by the Federal Reserve in accordance with the Bank Holding Company Act of 1956
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes
- **explanatoryNote**: According to the FFIEC, a bank holding company is a company that owns and/or controls one or more U.S. banks or one that owns, or has controlling interest in, one or more banks. A bank holding company may also own another bank holding company, which in turn owns or controls a bank; the company at the top of the ownership chain is called the top holder. The Board of Governors is responsible for regulating and supervising bank holding companies, even if the bank owned by the holding company is under the primary supervision of a different federal agency (OCC or FDIC).
- **explanatoryNote**: From the Bank Holding Company Act of 1956, a 'bank holding company' means any company (1) which directly or indirectly owns, controls, or holds with power to vote, 25 per centum or more of the voting shares of each of two or more banks or of a company which is or becomes a bank holding company by virtue of this Act, or (2) which controls in any manner the election of a majority of the directors of each of two or more banks, or (3) for the benefit of whose shareholders or members 25 per centum or more of the voting shares of each of two or more banks or a bank holding company is held by trustees; and for the purposes of this Act, any successor to any such company shall be deemed to be a bank holding company from the date as of which such predecessor company became a bank holding company. Notwithstanding the foregoing, (A) no bank shall be a bank holding company by virtue of its ownership or control of shares in a fiduciary capacity, except where such shares are held for the benefit of the shareholders of such bank, (B) no company shall be a bank holding company which is registered under the Investment Company Act of 1940, and was so registered prior to May 15, 1955 (or which is affiliated with any such company in such manner as to constitute an affiliated company within the meaning of such Act), unless such company (or such affiliated company), as the case may be, directly owns 25 per centum or more of the voting shares of each of two or more banks, (C) no company shall be a bank holding company by virtue of its ownership or control of shares acquired by it in connection with its underwriting of securities and which are held only for such period of time as will permit the sale thereof upon a reasonable basis, (D) no company formed for the sole purpose of participating in a proxy solicitation shall be a bank holding company by virtue of its control of voting rights of shares acquired in the course of such solicitation, and (E) no company shall be a bank holding company if at least 80 per centum of its total assets are composed of holdings in the field of agriculture.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
